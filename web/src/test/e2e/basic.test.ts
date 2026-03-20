import { test, expect } from '@playwright/test';

test('has title and omnibar', async ({ page }) => {
  await page.goto('/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Personal AI Core/);

  // Check if Omnibar is present
  const omnibar = page.locator('input[placeholder*="Ask anything"]');
  await expect(omnibar).toBeVisible();
});

test('sidebar has links', async ({ page }) => {
  await page.goto('/');
  
  const dashboardLink = page.getByRole('link', { name: /Dashboard/i });
  await expect(dashboardLink).toBeVisible();
});
