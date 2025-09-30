import { useState } from 'react';
import { generateProduct, Product } from '../helpers/product';
import ProductListItem from './ProductListItem';

type Props = {
    initialProducts: Product[];
};

/**
 * A component thst displays a list of products.
 *
 * @param {Product[]} props.initialItems The initial list of products to display
 * @returns {JSX.Element}
 */
export function ProductList({ initialProducts }: Props) {
    const [products, setProducts] = useState<Product[]>(initialProducts);

    const addProduct = () => {
        setProducts([...products, generateProduct()]);
    };

    return (
        <div className="product-list">
            <button onClick={addProduct}>Add product</button>

            {products.map((product) => (
                <ProductListItem key={product.name} product={product} />
            ))}
        </div>
    );
}
