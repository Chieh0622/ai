import gym

env = gym.make("CartPole-v1", render_mode = "human")
observation = env.reset(seed=42)

score = 0
for _ in range(1000):
    env.render()
    
    if observation[2] < 0:
        action = 0  # 向左移動
    else:
        action = 1  # 向右移動
    
    observation, reward, done, info = env.step(action)
    score += reward
    
    if done:
        observation = env.reset()
        print(f"Done, Score: {score}")
        score = 0
        
env.close()
