# Template: Robot Framework - Browser automation with Playwright

Want to build a [Playwright](https://playwright.dev/)-based browser robot? Great!

This template robot:

- Uses [Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework/basics) syntax.
- Includes all the necessary dependencies and initialization commands (`conda.yaml`).
- Solves the form challenge posted at http://rpachallenge.com. (`tasks.robot`).

## RPA Form challenge

The challenge consists of downloading an Excel spreadsheet, extracting the data from it and filling the form on the website with the data for ten times.

More in detail, when run, this robot will:

- download the test Excel file from the rpachallenge.com website
- collect the data from the downloaded Excel file
- start the challenge clicking on the Start button
- loop through the data and fill the forms for 10 times
- take a screenshot of the results page
- write log and report files
- close the browser

## Learning materials

- [Using the Robot Framework Browser library, based on Playwright](https://robocorp.com/docs/development-guide/browser/playwright)
