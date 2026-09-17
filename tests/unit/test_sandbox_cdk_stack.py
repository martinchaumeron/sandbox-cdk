import aws_cdk as core
import aws_cdk.assertions as assertions

from sandbox_cdk.sandbox_cdk_stack import SandboxCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sandbox_cdk/sandbox_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SandboxCdkStack(app, "sandbox-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
