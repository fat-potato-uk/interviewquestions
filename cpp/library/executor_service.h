#pragma once

#include <string>
#include <functional>

namespace library {

class ExecutorService {
public:
    // This function executes the provided function if a different thread
    void executeFunctionInAnotherThread(std::function<void()> && function);
};

}