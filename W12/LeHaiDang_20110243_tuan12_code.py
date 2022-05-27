#%%
import gym
#%%
if __name__ == "__main__":
    # env = gym.make("Acrobot-v1")
    # env = gym.make("MountainCar-v0")
    env = gym.make("MountainCarContinuous-v0")



    obs = env.reset()
    total_reward = 0
    while True:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)

        print("Action: ")
        print(action)
        print("Reward: %.2f. Observation: " % (reward))
        print(obs)

        env.render()
        total_reward += reward
        if done:
            env.close()
            break
    print("Done. Total_reward: ", total_reward)
# %%
