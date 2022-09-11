import { ApolloClient, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
    uri: "http://map-app:8000/graphql",
    cache: new InMemoryCache(),
});

export default client;