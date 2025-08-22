#include "concurrency_interview_questions.h"

#include "library/executor_service.h"
#include "library/update_callback.h"

#include <chrono>
#include <thread>
#include <utility>

using library::Update;
using library::UpdateCallback;

ConcurrencyInterviewQuestions::ConcurrencyInterviewQuestions(
    std::unique_ptr<UpdateCallback> && callback,
    std::reference_wrapper<library::ExecutorService> && executor)
: executor_{std::move(executor)},
  update_callback_{std::move(callback)},
  current_updates_{},
  currently_updating_{false},
  mutex_{}
{
    // Do Nothing
}

/*
 * This function is called by a gRPC request. Prevents downstream system
 * from receiving multiple updates one after another (by only sending one at max every 5 seconds).
 * The last update received is the one that is sent.
 * @param update the update received from the posting service
 */
void ConcurrencyInterviewQuestions::processUpdate(const Update & update)
{
    mutex_.lock();
    // We are happy with the data, so set it to our current record for this service
    current_updates_[update.name] = update;
    // If there is no scheduled task for the future, create one, otherwise finish
    if (!currently_updating_) {
        currently_updating_ = true;
        executor_.get().schedule([&]() {
            doUpdate();
        }, std::chrono::seconds(5));
    }

    mutex_.unlock();
}

void ConcurrencyInterviewQuestions::doUpdate()
{
    update_callback_->sendCallback(current_updates_);
    currently_updating_ = false;
    current_updates_.clear();
}