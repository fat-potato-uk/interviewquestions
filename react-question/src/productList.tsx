import { useState } from 'react';
import { generateProduct, IProduct } from './product';
import { ProductListItem } from './productListItem';

interface IProductListProps {
    initialProducts: IProduct[];
}

export function ProductList(props: IProductListProps) {
  const [products, setProducts] = useState<IProduct[]>(props.initialProducts);
  const refreshProducts = () => {
      setProducts([...products,  generateProduct()]);
  };
  
  return <div>
    <button onClick={refreshProducts}>Refresh</button>
    { products.map((product) => <ProductListItem key={product.name} product={product} /> )}
  </div>
}
