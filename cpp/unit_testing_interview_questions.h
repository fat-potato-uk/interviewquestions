#pragma once

#include <stdexcept>
#include <memory>

namespace testing_questions {

class TemperatureConstantGetter {
public:
    virtual ~TemperatureConstantGetter() = default;

    virtual int getHotnessConstant() const = 0;
    virtual int getHumidityConstant() const = 0;
};

enum class Animal {
    LION,
    POLAR_BEAR,
    CHINCHILLA
};

class ItsFarTooHotException : public std::runtime_error {
public:
    ItsFarTooHotException(const std::string & message)
        : std::runtime_error(message)
    { }

    const char * what() const noexcept override {
        return runtime_error::what();
    }
};

class UnitTestingInterviewQuestions {
public:
    explicit UnitTestingInterviewQuestions(std::shared_ptr<TemperatureConstantGetter> temperature_constant_getter);
    bool isItTooHot(int temperature, int humidity, Animal animal) const;

    // Made public just for testing, DO NOT USE
    int generateHotnessRating(int temperature, int humidity) const;

private:
    int calculateHumidityRating(int humidity) const;

    std::shared_ptr<TemperatureConstantGetter> temperature_constant_getter_;
};

}
