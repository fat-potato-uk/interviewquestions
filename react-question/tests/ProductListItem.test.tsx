import '@testing-library/jest-dom';

import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';

import { beforeEach } from 'node:test';
import ProductListItem from '../src/components/ProductListItem';
import * as Helpers from '../src/helpers/product';
import { generateProduct } from '../src/helpers/product';

vi.mock('../src/helpers/product');
const mockGenerateProduct = vi.mocked(generateProduct);

const MOCK_PRODUCT = {
    name: 'My test product',
    numberOfAvailableItems: 7
};

describe('ProductListItem', () => {
    beforeEach(() => {
        vi.resetAllMocks();
    });

    it('renders a product', () => {
        // When we return a mock product
        mockGenerateProduct.mockReturnValueOnce(MOCK_PRODUCT);

        // And we render the component ProductListItem
        render(<ProductListItem product={generateProduct()} />);

        // We can see the product title
        expect(screen.getByText('My test product')).toBeInTheDocument();

        // And the amount left
        expect(screen.getByText('Only 7 left!')).toBeInTheDocument();

        // And the buy now button
        expect(screen.getByRole('button', { name: 'Buy now!' })).toBeInTheDocument();
    });

    it('can buy a product', async () => {
        // When we return a mock product
        mockGenerateProduct.mockReturnValueOnce(MOCK_PRODUCT);

        const buyProductSpy = vi.spyOn(Helpers, 'buyProduct');
        const user = userEvent.setup();

        // And we render the component ProductListItem
        render(<ProductListItem product={generateProduct()} />);

        // When the buy now button is clicked
        await user.click(screen.getByRole('button', { name: 'Buy now!' }));

        // It calls the buy product function with the correct product
        expect(buyProductSpy).toHaveBeenCalledWith(MOCK_PRODUCT);
    });
});
