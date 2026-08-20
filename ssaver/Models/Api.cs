namespace ssaver.Models;
using System.Net.Http;
using System.Text.Json;

public class Api
{
    int send(string username, string repo, string file, string token)
    {
        HttpClient client = new HttpClient();
        string data = @" [ {""username"": ""John Doe"", ""occupation"": ""gardener""}, {""name"": ""Peter Novak"", ""occupation"": ""driver""} ]";
        using JsonDocument doc = JsonDocument.Parse(data);
        JsonElement root = doc.RootElement;
    }
}