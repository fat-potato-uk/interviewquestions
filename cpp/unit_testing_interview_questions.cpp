#include "unit_testing_interview_questions.h"

using namespace testing_questions;

UnitTestingInterviewQuestions::UnitTestingInterviewQuestions(std::shared_ptr<TemperatureConstantGetter> temperature_constant_getter)
    : temperature_constant_getter_{temperature_constant_getter}
{}

bool UnitTestingInterviewQuestions::isItTooHot(int temperature, int humidity, Animal animal) const {
    auto hotness_rating = generateHotnessRating(temperature, humidity);
    if(hotness_rating > 100) {
        throw ItsFarTooHotException("Too hot for animal");
    }

    switch(animal) {
    case Animal::LION:
        return hotness_rating > 70;
    case Animal::POLAR_BEAR:
        return hotness_rating > 10;
    case Animal::CHINCHILLA:
        return hotness_rating > 30;
    }
    throw ItsFarTooHotException("Invalid animal");
}

int UnitTestingInterviewQuestions::generateHotnessRating(int temperature, int humidity) const {
    auto humidity_rating = calculateHumidityRating(humidity);
    return (temperature * humidity_rating) / temperature_constant_getter_->getHotnessConstant();
}

int UnitTestingInterviewQuestions::calculateHumidityRating(int humidity) const {
    // TODO: More complex maths
    return humidity * temperature_constant_getter_->getHumidityConstant();
}
