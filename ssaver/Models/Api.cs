namespace ssaver.Models;
using System.Net.Http;
using System.Text.Json;

public class Api
{
    int send(string username, string repo, string file, string token)
    {
        HttpClient client = new HttpClient();
        string data = $@" [ {{""username"": ""{username}"", ""repo"": ""{repo}"",""file"",""{file}"",""token"",""{token}""}}]";
        using JsonDocument doc = JsonDocument.Parse(data);
        HttpResponseMessage response =
            await client.PostAsync("soon", content);
    }
}