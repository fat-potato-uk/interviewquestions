import { Animal } from './models/Animal';
import { ItsFarTooHotError } from './models/ItsFarTooHotError';
import { TemperatureConstantGetter } from './helpers/TemperatureConstantGetter';

export class UnitTestingInterviewQuestions {
    private temperatureConstantGetter: TemperatureConstantGetter;

    constructor(temperatureConstantGetter: TemperatureConstantGetter) {
        this.temperatureConstantGetter = temperatureConstantGetter;
    }

    async isItTooHot(temperature: number, humidity: number, animal: Animal): Promise<boolean> {
        if (temperature > 100) {
            throw new ItsFarTooHotError();
        }
        const hotnessRating = await this.generateHotnessRating(temperature, humidity);
        switch (animal) {
            case Animal.LION:
                return hotnessRating > 70;
            case Animal.POLAR_BEAR:
                return hotnessRating > 10;
            case Animal.CHINCHILLA:
                return hotnessRating > 30;
        }
    }

    async generateHotnessRating(temperature: number, humidity: number): Promise<number> {
        // TODO: Some additional maths that makes this function very long and complex
        const humidityRating = await this.calculateHumidityRating(humidity);
        return (temperature * humidityRating) / (await this.temperatureConstantGetter.getHotnessConstant());
    }

    private async calculateHumidityRating(humidity: number): Promise<number> {
        // TODO: More complex maths
        return humidity * (await this.temperatureConstantGetter.getHumidityConstant());
    }
}
