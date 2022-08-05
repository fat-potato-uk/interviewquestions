import React from 'react';
import ReactDOM from 'react-dom/client';
import { generateProduct } from './product';
import { IProduct } from './product';
import ProductList from './productList';

const initialItems: IProduct[] = Array.from({length: 25 }, () => generateProduct());

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <ProductList initialProducts={initialItems} />
  </React.StrictMode>
);
