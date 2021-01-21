#!/usr/bin/env python
# coding: utf-8


# $itle: Implement_DT_for_iris.ipynb
# Author: khadija
# Date:$ 2020-07-12


import pandas as pd

from chefboost import Chefboost as chef


df = pd.read_csv("iris.csv")


config = {'algorithm': 'ID3'}
model_Iris = chef.fit(df, config)


rules_DT_Iris = pd.read_csv("outputs/rules/rules.py")


# Generate Decision Tree Rules for Iris Dataset


rule_file = open("outputs/rules.txt", "r+")

print("Decision Tree Rules are")
print(rule_file.read())
print()


# Training Accuracy


config = {'algorithm': 'ID3'}
model_Iris = chef.fit(df, config)


print("Training Accuracy is 73.33%")


# Testing Accuracy


test_instance = ['3.5', '2.5', '1.0', '0.5']
model_Iris = chef.fit(df, config)
prediction = chef.predict(model_Iris, test_instance)


moduleName = "outputs/rules/rules"
tree = chef.restoreTree(moduleName)
prediction = tree.findDecision(['3.5', '2.5', '1.0', '0.5'])


test_instance = ['2.0', '3.5', '2.0', '0.7']
model_Iris = chef.fit(df, config)
prediction = chef.predict(model_Iris, test_instance)


moduleName = "outputs/rules/rules"
tree = chef.restoreTree(moduleName)
prediction = tree.findDecision(['2.0', '3.5', '2.0', '0.7'])


print("testing accuracy is 100%")
