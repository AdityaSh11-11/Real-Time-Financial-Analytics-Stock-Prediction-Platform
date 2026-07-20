"""
model.py

Machine Learning Service

Random Forest
Model Persistence
Prediction
Evaluation
"""

from __future__ import annotations

import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from config import FEATURE_COLUMNS


MODEL_PATH = "models/random_forest.pkl"


class ModelService:

    def __init__(self):

        os.makedirs("models", exist_ok=True)

        self.model = RandomForestClassifier(

            n_estimators=200,

            max_depth=10,

            random_state=42,

            n_jobs=-1

        )

    # ----------------------------------------

    def train(self, df):

        X = df[FEATURE_COLUMNS]

        y = df["Target"]

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=42,

            shuffle=False

        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        probability = self.model.predict_proba(X_test)

        metrics = {

            "accuracy": accuracy_score(

                y_test,

                predictions

            ),

            "precision": precision_score(

                y_test,

                predictions,

                zero_division=0

            ),

            "recall": recall_score(

                y_test,

                predictions,

                zero_division=0

            ),

            "f1": f1_score(

                y_test,

                predictions,

                zero_division=0

            ),

            "confusion_matrix": confusion_matrix(

                y_test,

                predictions

            )

        }

        self.save()

        return metrics

    # ----------------------------------------

    def predict(self, latest_row):

        X = latest_row[FEATURE_COLUMNS]

        prediction = self.model.predict(X)[0]

        confidence = self.model.predict_proba(X)[0].max()

        return prediction, confidence

    # ----------------------------------------

    def feature_importance(self):

        return self.model.feature_importances_

    # ----------------------------------------

    def save(self):

        joblib.dump(

            self.model,

            MODEL_PATH

        )

    # ----------------------------------------

    def load(self):

        if os.path.exists(MODEL_PATH):

            self.model = joblib.load(

                MODEL_PATH

            )

            return True

        return False