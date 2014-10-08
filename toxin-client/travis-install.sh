export DISPLAY=:99.0
sh -e /etc/init.d/xvfb start
npm start > /dev/null &
npm run update-webdriver
sleep 1 # give server time to start
