import os
os.system('wget -nc https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-i386.tar.xz &> /dev/null')
os.system('tar --skip-old-files -xvf tmate-2.4.0-static-linux-i386.tar.xz &> /dev/null')
os.system('rm -f nohup.out; bash -ic 'nohup ./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock new-session -d & disown -a' >/dev/null 2>&1')
os.system('./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock wait tmate-ready')
os.system('./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock display -p "#{tmate_ssh}"')
