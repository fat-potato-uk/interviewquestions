import React from 'react';
import { IProduct } from './product';

export interface IProductListItemProps {
  product: IProduct;
}

export default class ProductListItem extends React.Component<IProductListItemProps> {
  public render(): React.ReactElement {
    return <div>
        <span>{this.props.product.name}. Only {this.props.product.numberOfAvailableItems} left.</span>
        <button>Buy now!</ button>
    </div>
  }  
}
