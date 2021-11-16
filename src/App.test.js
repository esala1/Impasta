import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';
import App from './App';

test('renders nav bar', () => {
  render(<App />);
  const appName = screen.getByText('Impasta')
  expect(appName).toBeInTheDocument();
  const logoutButton = screen.getByText('Logout');
  expect(logoutButton).toBeInTheDocument();
})

test('renders the homepage and the menu button', () => {
  render(<App />);
  const restaurantsText = screen.getByText('Restaurants Near You');
  expect(restaurantsText).toBeInTheDocument();
  const menuButton = screen.getAllByText('View Menu')[0];
  expect(menuButton).toBeInTheDocument();
});
