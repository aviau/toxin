export DISPLAY=:99.0
sh -e /etc/init.d/xvfb start
npm start > /dev/null &
npm run update-webdriver
sleep 1 # give server time to start
node_modules/.bin/karma start karma.conf.js --no-auto-watch --single-run --reporters=dots --browsers=Firefox ; fi
node_modules/.bin/protractor e2e-tests/protractor.conf.js --browser=firefox ; fi
