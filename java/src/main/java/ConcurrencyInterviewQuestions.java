import lombok.Synchronized;
import models.Update;
import models.UpdateCallback;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

class ConcurrencyInterviewQuestions {

    /** This is the bean the client must implement to handle the update */
    private final UpdateCallback updateCallback;

    /** A map that stores the most current updates */
    private final Map<String, Update> currentUpdates = new HashMap<>();

    /** A scheduler for creating tasks in the future for sending the update */
    private final ScheduledExecutorService scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();

    /** The scheduled task that executes the call to the client */
    private Runnable scheduledTask;

    public ConcurrencyInterviewQuestions(UpdateCallback updateCallback) {
        this.updateCallback = updateCallback;
    }

    /**
     * This function is called by a HTTP POST handled in a RestController. Prevents downstream system
     * from receiving multiple updates one after another (by only sending one at max every 5 seconds).
     * The last update received is the one that is sent.
     * @param update the update received from the posting service
     */
    @Synchronized
    public void processUpdate(Update update) {
        // We are happy with the data, so set it to our current record for this service
        this.currentUpdates.put(update.getName(), update);

        // If there is no scheduled task for the future, create one, otherwise finish
        if(scheduledTask == null) {
            scheduledTask = this::doUpdate; // a lambda function -> the same as () -> this.doUpdate();
            scheduledExecutorService.schedule(scheduledTask, 5, TimeUnit.SECONDS);
        }
    }

    void doUpdate() {
        updateCallback.sendCallback(currentUpdates);
        scheduledTask = null;
        this.currentUpdates.clear();
    }
}
