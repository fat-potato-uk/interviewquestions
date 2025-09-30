import { buyProduct, Product } from '../helpers/product';

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
    return (
        <div className="product-item">
            <b>{product.name}</b>

            <div className="product-item-buy">
                <p>Only {product.numberOfAvailableItems} left!</p>
                <button onClick={() => buyProduct(product)}>Buy now!</button>
            </div>
        </div>
    );
};

export default ProductListItem;
