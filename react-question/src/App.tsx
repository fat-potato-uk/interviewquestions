import ProductList from './components/ProductList';
import { generateProduct } from './helpers/product';

const App = () => {
    const initialProducts = Array.from({ length: 10 }, () => generateProduct());

    return (
        <>
            <h1>Fat Potato Shop</h1>
            <ProductList initialProducts={initialProducts} />
        </>
    );
};

export default App;
