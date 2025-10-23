KonectIQ: The Technical Hygiene Manager for Multi-Cloud SMEs

🛠 Project Status: Actively Developing (Alpha)

🚀 Overview

KonectIQ is a purpose-built Multi-Cloud Management tool we are building that is focused on driving immediate, actionable Cost Savings and Security Improvements for Small and Medium Enterprises (SMEs), particularly those operating in the African market.

We are currently developing the core functionality that cuts through the complexity of enterprise-grade FinOps platforms to provide a simple, powerful solution for Technical Hygiene. Our goal is simple: to stop cloud waste and close critical security risks without requiring an expensive expert.

💡 Why KonectIQ?

Traditional cloud management tools are often too complex, require too many permissions, or focus on financial forecasting (FinOps). KonectIQ focuses on the quick wins that are often missed: idle servers, over-provisioned machines, and exposed security vulnerabilities.

We are read-only by design, meaning KonectIQ only provides highly accurate recommendations—the final implementation is always in your control.

✨ Key Features

1. SkyEdge™ AI Engine

Our proprietary engine continuously scans your connected cloud accounts (AWS, Azure, GCP) to identify two core areas of waste and risk:

Cloud Waste Detection: Finds resources that are running but idle (ghost servers), are sized too large for their usage (over-provisioning), or have been orphaned (unattached storage).

Cost Projection: Calculates the exact dollar amount you will save if you implement the recommended fix.

2. Shield™ Security Recommendations

KonectIQ automatically checks for critical, high-impact security misconfigurations that often lead to data breaches:

Public Access: Identifies storage buckets, databases, or network ports publicly exposed to the internet.

Vulnerability Alerts: Flags resources running on outdated operating systems or versions.

3. Actionable Dashboard

Instead of complex reports, KonectIQ presents the Top 3 Fixes on a clean, single dashboard, prioritizing recommendations by maximum cost savings or highest security risk.

Category

Problem

KonectIQ Recommendation

Estimated Monthly Savings

Cost

web-app-vm-dev running 24/7.

Implement a schedule to shut down the VM outside of business hours.

$78.00

Security

customer-data-s3-bucket public write access.

Change bucket policy to private (immediate fix).

Risk Closed

Cost

staging-db-01 has been idle for 60 days.

Terminate the resource and associated volumes.

$22.50

🛠 Technology Stack

KonectIQ is a modern, single-page application built for speed and reliability.

Frontend: React (JSX) with Tailwind CSS for a fully responsive, modern user experience.

State Management: React Hooks and Context API for streamlined state.

Data Persistence (User & App State): Google Firestore, using a secure, collaborative model to store user and application configuration.

API Integration: Secure, non-modifying integration points with AWS, Azure, and GCP APIs (via proxy) to perform read-only resource discovery and metric analysis.

📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
