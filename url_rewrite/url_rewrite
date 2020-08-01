#!/usr/bin/env python3
import json
import sys
import os
import logging
import logging.handlers
import signal



class UrlRewrite:
  def __init__(self, fn, log, logc):
    self.conf_fn    = fn
    self.log        = log
    self.logc       = logc
    self.conf_mtime = 0.0
    self.conf_data  = {}
    self.read_conf()

  def read_conf(self):
    try:
      conf_mtime = os.path.getmtime(self.conf_fn)
    except FileNotFoundError:
      conf_mtime = 0.0
      self.log.error('config '+ self.conf_fn + ' not found rewrite table not changed')
    if conf_mtime != 0.0 and conf_mtime != self.conf_mtime:
      self.conf_mtime = conf_mtime
      with open(self.conf_fn) as fd:
        try:
          self.conf_data = json.load(fd)
          self.log.info('rewrite table loaded')
        except ValueError:
          self.log.error('syntax error in config '+ self.conf_fn + ' rewrite table not changed')

  def send_resp(self, s):
    self.read_conf()
    ss = s.strip().split()
    (di,h) = (1,ss[0]+' ') if ss[0].isdigit() else (0,'')
    if len(ss) <= 3 + di:
      self._send_resp(h + "BH\n")
      return

    if ss[ 3 + di] == "CONNECT":
      self._send_resp(h + "OK\n")
      return

    for sv, url in self.conf_data.items():
      if sv in ss[di]:
        self.logc.info(ss[di]+" -> " + url)
        self._send_resp(h + "OK url=\""+url+"\"\n")
        return
    self._send_resp(h + "OK\n")

  def _send_resp(self,s):
    sys.stdout.write(s)
    sys.stdout.flush()


  


def hup(sig, frame):
  ur.read_conf()
  log.info('hup')


if __name__ == "__main__":
  log = logging.getLogger('url_rewrite')
  log.setLevel(logging.INFO)
  fmt = logging.Formatter('%(name)s[%(process)d] %(message)s')
  logh = logging.handlers.SysLogHandler(address = '/dev/log')
  logh.setFormatter(fmt)
  log.addHandler(logh)
  log.info('started')
  logc = logging.getLogger('url_rewrite_log')
  logc.setLevel(logging.INFO)
  logch = logging.FileHandler(filename='/var/log/squid/url_rewrite.log', mode='a')
  fmtc = logging.Formatter("%(asctime)s %(message)s", '%b %d %H:%M:%S')
  logch.setFormatter(fmtc)
  logc.addHandler(logch)
  ur = UrlRewrite(sys.argv[1] if len(sys.argv) >= 2 else "/etc/squid/url_rewrite.conf",log,logc)
  signal.signal(signal.SIGHUP, hup)
  while True:
    s = sys.stdin.readline()
    if s == '':
      break
    ur.send_resp(s)
  log.info('exit')
