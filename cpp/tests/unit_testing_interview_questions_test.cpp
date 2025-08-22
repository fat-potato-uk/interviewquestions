#include "../unit_testing_interview_questions.h"

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include <memory>
#include <tuple>

using testing_questions::Animal;
using testing_questions::UnitTestingInterviewQuestions;

using testing::Return;

class MockTemperatureConstantGetter : public testing_questions::TemperatureConstantGetter {
public:
    MOCK_METHOD(int, getHotnessConstant, (), (const override));
    MOCK_METHOD(int, getHumidityConstant, (), (const override));
};

TEST(UnitTestingInterviewQuestionsTest, tooHotForLion) {
    auto mock = std::make_shared<MockTemperatureConstantGetter>();
    auto instance = UnitTestingInterviewQuestions{mock};

    EXPECT_CALL(*mock, getHotnessConstant()).Times(1).WillOnce(Return(100));
    EXPECT_CALL(*mock, getHumidityConstant()).Times(1).WillOnce(Return(100));
    EXPECT_TRUE(instance.isItTooHot(10, 10, Animal::LION));
}

TEST(UnitTestingInterviewQuestionsTest, notTooHotForLion) {
    auto mock = std::make_shared<MockTemperatureConstantGetter>();
    auto instance = UnitTestingInterviewQuestions{mock};

    EXPECT_CALL(*mock, getHotnessConstant()).Times(1).WillOnce(Return(40));
    EXPECT_CALL(*mock, getHumidityConstant()).Times(1).WillOnce(Return(5));
    EXPECT_FALSE(instance.isItTooHot(10, 20, Animal::LION));
}

class GenerateHotnessRatingTests : public testing::TestWithParam<std::tuple<int, int, int>> {
};

TEST_P(GenerateHotnessRatingTests, complexHotnessCalculationTest) {
    auto data = GetParam();
    auto mock = std::make_shared<MockTemperatureConstantGetter>();
    auto instance = UnitTestingInterviewQuestions{mock};

    EXPECT_CALL(*mock, getHotnessConstant()).Times(1).WillOnce(Return(10));
    EXPECT_CALL(*mock, getHumidityConstant()).Times(1).WillOnce(Return(1));

    auto temp = std::get<0>(data);
    auto humidity = std::get<1>(data);
    auto expected_result = std::get<2>(data);
    EXPECT_EQ(expected_result, instance.generateHotnessRating(temp, humidity));
}

INSTANTIATE_TEST_SUITE_P(complexHotnessCalculationTestData,
                         GenerateHotnessRatingTests,
                         testing::Values(
                            std::make_tuple(100, 20, 200),
                            std::make_tuple(-15, 20, -30),
                            std::make_tuple(20, 0 , 0)
                        ));
