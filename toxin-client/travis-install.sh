export DISPLAY=:99.0
sh -e /etc/init.d/xvfb start

curl https://raw.githubusercontent.com/creationix/nvm/v0.17.2/install.sh | bash
nvm install 0.10
nvm use 0.10
npm start > /dev/null &
npm run update-webdriver
sleep 1 # give server time to start
node_modules/.bin/karma start karma.conf.js --no-auto-watch --single-run --reporters=dots --browsers=Firefox
node_modules/.bin/protractor e2e-tests/protractor.conf.js --browser=firefox
