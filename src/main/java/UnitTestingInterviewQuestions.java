import models.Animal;
import helpers.TemperatureConstantGetter;
import models.ItsFarTooHotException;

public class UnitTestingInterviewQuestions {

    private final TemperatureConstantGetter temperatureConstantGetter;

    public UnitTestingInterviewQuestions(TemperatureConstantGetter temperatureConstantGetter) {
        this.temperatureConstantGetter = temperatureConstantGetter;
    }

    public boolean isItTooHot(int temperature, int humidity, Animal animal) throws ItsFarTooHotException {
        var hotnessRating = this.generateHotnessRating(temperature, humidity);

        if(hotnessRating > 100) {
            throw new ItsFarTooHotException();
        }

        return switch (animal) {
            case LION -> hotnessRating > 70;
            case POLAR_BEAR -> hotnessRating > 10;
            case CHINCHILLA -> hotnessRating > 30;
        };
    }

    int generateHotnessRating(int temperature, int humidity) {
        // TODO: Some additional maths that makes this function very long and complex
        var humidityRating = calculateHumidityRating(humidity);
        return (temperature * humidityRating) / this.temperatureConstantGetter.getHotnessConstant();
    }

    private int calculateHumidityRating(int humidity) {
        // TODO: More complex maths
        return humidity * this.temperatureConstantGetter.getHumidityConstant();
    }
}
