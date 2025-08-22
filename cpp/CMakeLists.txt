cmake_minimum_required(VERSION 3.28)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "-W -Wall -Werror")

project(interview_question_cpp)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
add_subdirectory(library)

add_library(${PROJECT_NAME} SHARED concurrency_interview_questions.cpp unit_testing_interview_questions.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC library)

include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/releases/download/v1.17.0/googletest-1.17.0.tar.gz
)
FetchContent_MakeAvailable(googletest)

add_subdirectory(tests)