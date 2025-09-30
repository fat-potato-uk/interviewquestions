import { useState } from 'react';
import { generateProduct, Product } from '../helpers/product';
import ProductListItem from './ProductListItem';

type Props = {
    initialProducts: Product[];
};

/**
 * A component that displays a list of products.
 *
 * @param {Product[]} props.initialItems The initial list of products to display
 * @returns {JSX.Element}
 */
export const ProductList = ({ initialProducts }: Props) => {
    const [products, setProducts] = useState<Product[]>(initialProducts);

    /**
     * Adds a new product to the end of the product list.
     */
    const addProduct = () => {
        const newProduct = generateProduct();
        setProducts([...products, newProduct]);
    };

    return (
        <div className="product-list">
            <button onClick={addProduct}>Add product</button>

            {products.map((product) => (
                <ProductListItem key={product.name} product={product} />
            ))}
        </div>
    );
};

export default ProductList;
