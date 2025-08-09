#!/usr/bin/env python3
from src.graph.gnn_training import train_node_classifier, train_link_prediction

if __name__ == "__main__":
    train_node_classifier()
    train_link_prediction()
    print("GNN training jobs completed.")
