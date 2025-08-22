#pragma once

#include <chrono>
#include <functional>

namespace library {

class ExecutorService {
public:
    /*
     * This function executes the provided function in a different thread
     * after the given delay has passed.
     * This function returns immediately! Both the delay and function happen
     * in another thread of execution and do not block the calling thread
     */
    void schedule(std::function<void()> && function,
                  std::chrono::seconds delay);
};

}