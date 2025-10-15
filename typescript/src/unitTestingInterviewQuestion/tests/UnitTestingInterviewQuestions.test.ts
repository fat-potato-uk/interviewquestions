import { vi, describe, it, expect, beforeEach } from 'vitest';
import { UnitTestingInterviewQuestions } from '../UnitTestingInterviewQuestions';
import { TemperatureConstantGetter } from '../helpers/TemperatureConstantGetter';
import { Animal } from '../models/Animal';

vi.mock('../helpers/TemperatureConstantGetter', () => {
    return {
        TemperatureConstantGetter: vi.fn().mockImplementation(() => {
            return {
                getHotnessConstant: vi.fn().mockResolvedValue(10),
                getHumidityConstant: vi.fn().mockResolvedValue(1)
            };
        })
    };
});

describe('UnitTestingInterviewQuestions', () => {
    // Component under test
    let unitTestingInterviewQuestions: UnitTestingInterviewQuestions;

    beforeEach(() => {
        unitTestingInterviewQuestions = new UnitTestingInterviewQuestions(new TemperatureConstantGetter());
    });

    describe('isItTooHot', () => {
        it('calculates if it is too hot', async () => {
            const generateHotnessRatingSpy = vi.spyOn(unitTestingInterviewQuestions, 'generateHotnessRating');

            generateHotnessRatingSpy.mockResolvedValue(80);
            expect(await unitTestingInterviewQuestions.isItTooHot(10, 10, Animal.LION)).toBe(true);

            generateHotnessRatingSpy.mockResolvedValue(50);
            expect(await unitTestingInterviewQuestions.isItTooHot(10, 10, Animal.LION)).toBe(false);
        });
    });

    describe('generates the correct hotness rating', () => {
        const doComplexHotnessCalculationArguments = [
            // Test our happy case
            { temp: 100, humidity: 20, result: 200 },
            // Test a negative temperature
            { temp: -15, humidity: 20, result: -30 },
            // Test an 0 value case
            { temp: 20, humidity: 0, result: 0 }
        ];

        it.each(doComplexHotnessCalculationArguments)(
            'generateHotnessRating ($temp, $humidity)',
            async ({ temp, humidity, result }) => {
                expect(result).equals(await unitTestingInterviewQuestions.generateHotnessRating(temp, humidity));
            }
        );
    });
});
