import React from 'react';
import ReactDOM from 'react-dom/client';
import { generateProduct } from './helpers/product';
import { Product } from './helpers/product';
import { ProductList } from './components/ProductList';

import './index.css';

const initialItems: Product[] = Array.from({ length: 10 }, () => generateProduct());

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);

root.render(
    <React.StrictMode>
        <h1>Fat Potato Shop</h1>
        <ProductList initialProducts={initialItems} />
    </React.StrictMode>
);
