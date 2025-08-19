#pragma once

#include "library/update.h"

#include <functional>
#include <map>
#include <memory>
#include <mutex>

namespace library {
    class ExecutorService;
    class UpdateCallback;
}

class ConcurrencyInterviewQuestions {
public:
    ConcurrencyInterviewQuestions(std::unique_ptr<library::UpdateCallback> && callback,
        std::reference_wrapper<library::ExecutorService> && executor);

    void processUpdate(const library::Update & update);

    ConcurrencyInterviewQuestions(const ConcurrencyInterviewQuestions&) = delete;
    ConcurrencyInterviewQuestions& operator=(const ConcurrencyInterviewQuestions&) = delete;
    ConcurrencyInterviewQuestions(ConcurrencyInterviewQuestions&&) = delete;
    ConcurrencyInterviewQuestions& operator=(ConcurrencyInterviewQuestions&&) = delete;

private:
    void doUpdate();

    // An executor service for executing tasks in other threads
    std::reference_wrapper<library::ExecutorService> executor_;
    // This is an instance of the UpdateCallback the client has implemented
    std::unique_ptr<library::UpdateCallback> update_callback_;
    // A map that stores the most current updates
    std::map<std::string, library::Update> current_updates_;
    // Is an update currently running
    bool currently_updating_;
    // Mutex to ensure thread safty
    std::mutex mutex_;
};
