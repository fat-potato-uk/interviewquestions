import { useState } from 'react';
import { generateProduct, IProduct } from './product';

interface IProductListProps {
    initialProducts: IProduct[];
}

interface IProductListItemProps {
  product: IProduct;
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

export function ProductListItem(props: IProductListItemProps): JSX.Element {
    return <div>
        <span>{props.product.name}. Only {props.product.numberOfAvailableItems} left.</span>
        <button>Buy now!</ button>
    </div>
}
