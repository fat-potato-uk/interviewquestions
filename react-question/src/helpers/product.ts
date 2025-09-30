import { faker } from '@faker-js/faker';

export type Product = {
    name: string;
    numberOfAvailableItems: number;
};

export function generateProduct(): Product {
    return {
        name: faker.commerce.product(),
        numberOfAvailableItems: Math.floor(Math.random() * 3) + 1
    };
}
