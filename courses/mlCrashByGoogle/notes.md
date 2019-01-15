# Machine Leaning crash course by Google

## 1. Intro to ML
ML changes the way you think about a problem.

## 2. Framing
How to frame a task as ML problem. 

**What is supervised ML?**
ML systems learn how to combine input to produce useful predictions on never-before-seen data.


1. **Example Data** - DataSet.
2. **Labeled Example** has {features, label}: (x, y) - Used to train the model. 
3. **Unlabeled Example** has {features, ? }: (x, ?) - Used for making predictions on new data.
4. **Model** maps example to predicted labels: y' - Defined by internal param whcich are learned.

For example, 
An example is a particular instance of data, x.We break examples into two categories:
1. Labeled examples
2. Unlabeled examples

 labeled example includes both feature(s) and the label. That is:
 ```python
   labeled examples: {features, label}: (x, y)
 ```
 | HousingMedianAge(feature) | TotalRooms (feature)|MedianHouseValue(label) |
 |----------|:-------------:|------ |
 | 15 | 25456 | 66900|
 | 19 | 7650 | 80100 |
 | 17 | 720 | 85700 |
 
 An unlabeled example contains features but not the label. That is:
 ```python
 unlabeled examples: {features, ?}: (x, ?)
 ```
 | HousingMedianAge(feature) | TotalRooms (feature)|
 |----------|:-------------:|
 | 67 | 902726 |
 | 28 | 89797  |
 | 80 | 776242 |
 
 **Model**:
1. A model defines the relationship between **features and label**. Training means creating or learning the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.

2. Inference means applying the **trained model to unlabeled examples**. That is, you use the trained model to make useful predictions (y'). For example, during inference, you can predict medianHouseValue for new unlabeled examples.

**Regression vs. classification**:
A regression model predicts **continuous values**.
* What is the value of a house in California?
* What is the probability that a user will click on this ad?

A classification model predicts **discrete values**.
* Is a given email message spam or not spam?
* Is this an image of a dog, a cat, or a hamster?

## 3. Descending into ML:

**Math Basics:**
What is variable?
a linear equation is an equation that may be put in the form,
$$ {a_1x_1 + a_2x_2 + ... + a_nx_n + b} = 0 $$

Where x1,x2..xn are the variable and b,a1,a2..an are the Coefficient and b is the bias.

![linerFunction](images/CricketLine.svg)

We could write it down like this,
$$ y = mx + b $$

Where,

 * y is the temperature in Celsius—the value we're trying to predict.
 * m is the slope of the line.
 * x is the number of chirps per minute—the value of our input feature.
 * b is the y-intercept.

By convention in machine learning, you'll write the equation for a model slightly differently:
$$ y' = b + w_1x_1 $$

Where,

* y' is the predicted label (a desired output).
* b  is the bias (the y-intercept), sometimes referred to as w0.
* w1 is the weight of feature 1. Weight is the same concept as the "slope" m in the traditional equation of a line.
* x1 is the feature(input).

Although this model uses only one feature, a more sophisticated model might rely on multiple features, each having a separate weight (w1, w2, etc.). For example, a model that relies on three features might look as follows:

$$ y' = b + w_1x_1 + w_2x_2 + w_3x_3 $$

**Training and Loss:**
Training a model simply means learning (determining) good values for all the weights and the bias from labeled examples. In supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called empirical risk minimization.

Loss is the penalty for a bad prediction. That is, loss is a number indicating how bad the model's prediction was on a single example. If the model's prediction is perfect, the loss is zero; otherwise, the loss is greater. The goal of training a model is to find a set of weights and biases that have low loss, on average, across all examples. For example, Figure 3 shows a high loss model on the left and a low loss model on the right. Note the following about the figure:

* The arrows represent loss.
* The lines represent predictions.

### Squared loss: a popular loss function:
The linear regression models we'll examine here use a loss function called squared loss (also known as L2 loss). The squared loss for a single example is as follows:

```python
  = the square of the difference between the label and the prediction
  = (observation - prediction(x))2
  = (y - y')2
```

Mean square error (MSE) is the average squared loss per example over the whole dataset. To calculate MSE, sum up all the squared losses for individual examples and then divide by the number of examples:

$$ MSE = \frac{1}{N} \sum_{(x,y)\in D} (y - prediction(x))^2 $$

Where,
* (x, y) is an example in which,
  * x is the set of features (for example, chirps/minute, age, gender) that the model uses to make predictions.
  * y is the example's label (for example, temperature).
* prediction(x) is a function of the weights and bias in combination with the set of features x.
* D is a data set containing many labeled examples, which are(x, y) pairs.
* N is the number of examples in D.

## 4. Reducing the Loss:

![GradientDescentDiagram](images/GradientDescentDiagram.svg)

The "model" takes one or more features as input and returns one prediction (y') as output. To simplify, consider a model that takes one feature and returns one prediction:

$$ y' = b + w_1x_1 $$

The "Compute Loss" part of the diagram is the loss function that the model will use. Suppose we use the squared loss function. The loss function takes in two input values:
* y': The model's prediction for features x.
* y: The correct label corresponding to features x.

**A Machine Learning model is trained by starting with an initial guess for the weights and bias and iteratively adjusting those guesses until learning the weights and bias with the lowest possible loss.**

### Reducing Loss: Gradient Descent:
![convex](images/convex.svg)

The first stage in gradient descent is to pick a starting value (a starting point) for w1. The starting point doesn't matter much; therefore, many algorithms simply set w1 to 0 or pick a random value. The following figure shows that we've picked a starting point slightly greater than 0:

![convex](images/GradientDescentStartingPoint.svg)

The gradient is a vector, so it has both of the following characteristics:
* a direction
* a magnitude

The gradient always points in the direction of steepest increase in the loss function. The gradient descent algorithm takes a step in the direction of the negative gradient in order to reduce loss as quickly as possible.

![GradientDescentNegativeGradient](images/GradientDescentNegativeGradient.svg)

To determine the next point along the loss function curve, the gradient descent algorithm adds some fraction of the gradient's magnitude to the starting point as shown in the following figure:

![GradientDescentGradientStep](images/GradientDescentGradientStep.svg)

**The gradient descent then repeats this process, edging ever closer to the minimum.**

---
**Note:** When performing gradient descent, we generalize the above process to tune all the model parameters simultaneously. For example, to find the optimal values of both w1 and the bias b, we calculate the gradients with respect to both w1 and b. Next, we modify the values of w1 and b based on their respective gradients. Then we repeat these steps until we reach minimum loss.

---
### Reducing Loss: Learning Rate:
As noted, the gradient vector has both a direction and a magnitude. Gradient descent algorithms multiply the gradient by a scalar known as the learning rate (also sometimes called step size) to determine the next point. For example, if the gradient magnitude is 2.5 and the learning rate is 0.01, then the gradient descent algorithm will pick the next point 0.025 away from the previous point.

![LearningRateTooSmall](images/LearningRateTooSmall.svg)

![LearningRateTooLarge](images/LearningRateTooLarge.svg)

![LearningRateJustRight](images/LearningRateJustRight.svg)

**Epoch vs Batch Size vs Iterations**
**Epoch:**
One Epoch is when an ENTIRE dataset is passed forward and backward through the neural network only ONCE.

**Batch Size:**
Total number of training examples present in a single batch. We can’t pass the entire dataset into the neural net at once. So, you divide dataset into Number of Batches or sets or parts.

**Iterations:**
Iterations is the number of batches needed to complete one epoch.

For example,
We can divide the dataset of 2000 examples into batches of 500 then it will take a 4 iterations to complete 1 epoch.

