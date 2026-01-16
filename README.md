KonectIQ v1: The Technical Hygiene Manager for Multi-Cloud SMEs
Unified Network, Security, and Backup Platform

KonectIQ is a modular control platform for MSPs (Managed Service Providers), independent consultants, and small IT teams operating in cost-sensitive environments.
It centralizes network management, security enforcement, and backup operations into a single, minimal control plane.

This repository represents v1. The focus is reliability, clarity, and operational value.

Purpose

KonectIQ exists to solve three practical problems for small operators:

Fragmented tooling across network, security, and backup

Manual processes that do not scale

Enterprise platforms that are too heavy, expensive, or complex

It provides one interface to manage, secure, and monitor distributed environments with minimal infrastructure.

Core Principles

Modular design: only use what you need

Automation first: reduce manual operational work

Low overhead: deployable on modest cloud or edge systems

Cost awareness: designed for budget-constrained environments

Operator focus: built for real production use, not demos

Modules (v1)

Only the following modules are supported:

CommandView™ – Central management and control

Pulse™ – Minimal dashboard for critical status and alerts

SecureMesh™ – Network segmentation and access control

Shield™ – Endpoint security and threat response

Vault™ – Backup and recovery management

DeviceScan™ – Network discovery and asset inventory

EdgeBox™ – Optional on-prem edge node

SkyEdge™ – Cloud edge services

PilotView™ – Read-only client visibility

Security and backup functions are powered by SkyLock Engine™, which integrates SASE (Secure Access Service Edge) and EDR (Endpoint Detection and Response) components.

Who This Is For

MSPs managing small to mid-size environments

Independent cloud, network, and security consultants

Teams in bandwidth-limited or cost-constrained regions

Not intended for:

General ITSM platforms

Full SOC (Security Operations Center) workflows

Custom application development frameworks

Deployment

KonectIQ v1 supports two practical models:

Cloud-Hosted

Single VM or container host

Central management for multiple clients

Lowest operational overhead

Edge Deployment (EdgeBox™)

Small on-prem device

Designed for unreliable or limited connectivity

Syncs with CommandView™ when online

What v1 Provides

Centralized visibility across networks and devices

Automated discovery and monitoring

Policy-based security and access controls

Integrated backup and recovery management

A deliberately minimal dashboard focused on operational signals

What it does not attempt:

Full SOC functionality

Broad ITSM workflows

Developer-oriented extensibility

High-Level Usage

Deploy CommandView™ (cloud or EdgeBox™)

Connect sites using SecureMesh™

Discover assets with DeviceScan™

Enable protection via Shield™ and Vault™

Monitor through Pulse™

Detailed operational guides and playbooks are maintained outside this repository.

Roadmap Direction

KonectIQ will remain:

Lean in interface

Modular in architecture

Focused on automation and security

Built for solo founders and small MSP teams

Future releases will expand integrations and reporting without increasing complexity.

License

Proprietary Software

This software is not open source.

Source code is provided for evaluation, review, or authorized deployment only.

Modification, redistribution, commercial hosting, or use in managed service offerings is not permitted without a valid license.

All rights reserved.

For licensing, partnerships, or commercial use, contact:
sales@designx.co.ke
