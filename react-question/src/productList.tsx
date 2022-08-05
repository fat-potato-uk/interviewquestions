import React from 'react';
import { generateProduct, IProduct } from './product';
import ProductListItem from './productListItem';

interface IProductListProps {
    initialProducts: IProduct[];
}

interface IProductListState {
    products: IProduct[];
}

export default class ProductList extends React.Component<IProductListProps, IProductListState> {
  constructor(props: IProductListProps) {
    super(props);

    this.refreshClicked = this.refreshClicked.bind(this);

    this.state = {
      products: this.props.initialProducts
    };
  }
  
  public render(): React.ReactElement {
    return <div>
      <button onClick={this.refreshClicked}>Refresh</button>
      { this.state.products.map((product) => <ProductListItem key={product.name} product={product} /> )}
    </div>
  }

  private refreshClicked(): void {
    this.setState({
      products: [...this.state.products,  generateProduct()]
    });
  }
}