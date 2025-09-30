import { Product } from '../helpers/product';

type Props = {
    product: Product;
};

/**
 * A component that shows an individual product
 *
 * @param {Product} props.product The product to display
 * @returns {JSX.Element}
 */
const ProductListItem = ({ product }: Props) => {
    const buyProduct = () => {
        // Mock API call to buy product...
    };

    return (
        <div className="product-item">
            <b>{product.name}</b>

            <div className="product-item-buy">
                <p>Only {product.numberOfAvailableItems} left!</p>
                <button onClick={buyProduct}>Buy now!</button>
            </div>
        </div>
    );
};

export default ProductListItem;
