cmake_minimum_required(VERSION 3.28)

include(GoogleTest)
enable_testing()

add_executable(unit_tests unit_testing_interview_questions_test.cpp ../unit_testing_interview_questions.cpp)
target_link_libraries(unit_tests GTest::gtest_main GTest::gmock_main library)

gtest_discover_tests(unit_tests)