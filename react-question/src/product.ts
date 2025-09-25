import { faker } from '@faker-js/faker';

export interface IProduct {
    name: string;
    numberOfAvailableItems: number;
}

export function generateProduct(): IProduct {
    return {
        name: faker.commerce.productName(),
        numberOfAvailableItems: Math.floor(Math.random() * 3) + 1
    };
}
