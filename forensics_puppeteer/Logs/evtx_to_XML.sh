#! /bin/zsh

for f in ./*.evtx do
    python3 /opt/python-evtx/scripts/evtx_dump.py evtx_dump.py "`$f`" > ../XML_logs/`$f`.xml
done

