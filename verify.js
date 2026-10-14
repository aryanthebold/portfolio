const { chromium } = require('playwright');
const path = require('path');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const filePath = 'file://' + path.resolve(__dirname, 'index.html');

    await page.goto(filePath);

    // Test Escape Key Dismissal
    console.log('Testing Escape Key Dismissal...');
    const card = page.locator('.fc').first();

    // Open card
    await card.click({ force: true });
    await page.waitForTimeout(500); // Wait for transition
    const isExpandedBefore = await card.evaluate(el => el.classList.contains('expanded'));
    if (!isExpandedBefore) throw new Error('Card did not expand on click.');

    // Press escape
    await page.keyboard.press('Escape');
    await page.waitForTimeout(500); // Wait for transition
    const isExpandedAfter = await card.evaluate(el => el.classList.contains('expanded'));
    if (isExpandedAfter) throw new Error('Card did not close on Escape key.');

    console.log('Escape Key Dismissal successful.');

    // Verify Focus states applied
    console.log('Testing Focus Visibility...');
    await page.keyboard.press('Tab'); // First element should be the first card
    const focusedOutline = await card.evaluate(el => window.getComputedStyle(el).outlineStyle);
    if(focusedOutline === 'none') {
        throw new Error('Focus outline not found on .fc element.');
    }

    console.log('Focus Visibility successful.');

    await browser.close();
})();
