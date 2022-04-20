import graphene


class UpdateStatus(graphene.Mutation):
    class Arguments:
        status = graphene.String()

    ok = graphene.Boolean()

    def mutate(root, info, status):
        user = info.context.user
        user.status = status
        return UpdateStatus(ok=True)


class ProfileMutation(graphene.ObjectType):
    change_status = UpdateStatus.Field()