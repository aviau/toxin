export DISPLAY=:99.0
sh -e /etc/init.d/xvfb start
nvm install 0.10
npm start > /dev/null &
npm run update-webdriver
sleep 1 # give server time to start
npm run protractor
