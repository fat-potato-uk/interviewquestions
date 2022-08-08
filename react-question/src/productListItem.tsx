import { IProduct } from './product';

export interface IProductListItemProps {
  product: IProduct;
}

export function ProductListItem(props: IProductListItemProps): JSX.Element {
    return <div>
        <span>{props.product.name}. Only {props.product.numberOfAvailableItems} left.</span>
        <button>Buy now!</ button>
    </div>
}
