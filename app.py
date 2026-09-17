#!/usr/bin/env python3
import aws_cdk as cdk

from sandbox_cdk.sandbox_cdk_stack import SandboxCdkStack


app = cdk.App()
SandboxCdkStack(
    app,
    "SandboxCdkStack",
    env=cdk.Environment(account="187478112166", region="eu-west-3"),
)

app.synth()